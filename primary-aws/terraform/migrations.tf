moved {
  from = aws_vpc_security_group_ingress_rule.wireguard_peer
  to   = aws_vpc_security_group_ingress_rule.wireguard_peer["peer"]
}
