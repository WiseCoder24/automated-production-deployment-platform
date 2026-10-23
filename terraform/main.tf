terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "app" {
  name                 = "automated-production-deployment-platform"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  encryption_configuration {
    encryption_type = "AES256"
  }

  tags = {
    Project     = "automated-production-deployment-platform"
    Environment = "lab"
    ManagedBy   = "Terraform"
  }
}

output "ecr_repository_url" {
  description = "URI used by Docker to tag and push the application image"
  value       = aws_ecr_repository.app.repository_url
}
