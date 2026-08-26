from __future__ import annotations

import re
import unittest

from _cicd_lib import SECURITY_GROUPS, read


class SecurityGroupAllowlistContractTests(unittest.TestCase):
    def test_declared_public_ingress_is_exactly_the_p2p_allowlist(self) -> None:
        expected = {
            "el_p2p_tcp": ("tcp", 30303),
            "el_p2p_udp": ("udp", 30303),
            "cl_p2p_tcp": ("tcp", 9000),
            "cl_p2p_udp": ("udp", 9000),
            "cl_quic_udp": ("udp", 9001),
        }
        blocks = re.findall(
            r'resource "aws_vpc_security_group_ingress_rule" "([^"]+)" \{(.*?)\n\}',
            read(SECURITY_GROUPS),
            flags=re.DOTALL,
        )
        public = {
            name: block
            for name, block in blocks
            if 'cidr_ipv4         = "0.0.0.0/0"' in block
        }
        self.assertEqual(set(public), set(expected))

        for name, (protocol, port) in expected.items():
            with self.subTest(name=name):
                self.assertIn(f'ip_protocol       = "{protocol}"', public[name])
                self.assertIn(f"from_port         = {port}", public[name])
                self.assertIn(f"to_port           = {port}", public[name])


if __name__ == "__main__":
    unittest.main()
