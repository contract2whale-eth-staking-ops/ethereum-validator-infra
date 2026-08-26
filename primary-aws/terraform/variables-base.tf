variable "network" {
  description = "대상 네트워크"
  type        = string
  default     = "hoodi"

  validation {
    condition     = contains(["hoodi", "mainnet"], var.network)
    error_message = "network must be hoodi or mainnet."
  }
}

variable "region" {
  description = "주노드 리전"
  type        = string
  default     = "ap-northeast-2"
}

variable "kms_recovery_region" {
  description = "복구용 KMS 리전"
  type        = string
  default     = "eu-central-1"

  validation {
    condition     = var.kms_recovery_region != var.region
    error_message = "recovery KMS region must differ from the primary region."
  }
}

variable "allow_protected_destroy" {
  description = "보호 리소스 teardown 승인값"
  type        = bool
  default     = false
}

variable "enable_staging_bucket" {
  description = "암호문 staging bucket 사용 여부"
  type        = bool
  default     = true
}
