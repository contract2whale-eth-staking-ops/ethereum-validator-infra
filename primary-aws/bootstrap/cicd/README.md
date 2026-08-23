# GitHub OIDC와 Terraform CI/CD 부트스트랩

이 README는 강의 영상에서 현재 디렉터리의 파일을 사용할 때 함께 보는 실행 참조서입니다. 명령은 저장소 루트에서 실행하며, AWS Console과 GitHub 화면의 설명은 강의를 따릅니다.

각 단계는 위에서 아래 순서로 진행합니다. 현재 단계의 완료 확인이 끝난 뒤 다음 단계로 이동합니다.

## 1. OIDC와 Terraform 배포 경계

- Stage: `G2`

### 사용할 파일

- `primary-aws/bootstrap/`
- `.github/workflows/terraform-deploy.yml`
- `primary-aws/terraform/ci/runtime-inputs.json`

### 실행

저장소 루트에서 아래 명령을 위에서부터 실행합니다.

```bash
source ./lab.env
aws sso login --profile "${PLATFORM_BOOTSTRAP_AWS_PROFILE}"
aws cloudformation validate-template --template-body file://primary-aws/bootstrap/cicd/template.yaml --profile "${PLATFORM_BOOTSTRAP_AWS_PROFILE}"
python3 -m unittest tests/test_terraform_deploy_contract.py
```

### 완료 확인

GitHub OIDC provider, PlanRole, ApplyRole와 backend가 생성되고 Platform Admin 임시 assignment가 회수된 상태

## CloudFormation output 기록 위치

부트스트랩 stack의 output을 `primary-aws/terraform/ci/runtime-inputs.json`에 기록합니다.

| CloudFormation output | runtime manifest field |
|---|---|
| `NodePermissionsBoundaryArn` | `.aws.node_permissions_boundary_arn` |
| `KmsBreakGlassRoleArn` | `.aws.kms_break_glass_role_arn` |
| `NodeSshKeyPairName` | `.terraform.key_pair_name` |

기록 후 `shared/scripts/render-terraform-ci-runtime.py`로 manifest를 검증합니다. GitHub `hoodi-testnet-dev`와 `hoodi-testnet-dev-teardown` Environment는 승인 경계만 사용하므로 Environment variables/secrets 0개를 유지합니다.
