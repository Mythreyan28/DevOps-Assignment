terraform {
  backend "s3" {
    bucket         = "devops-tf-state-1770900240"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}

