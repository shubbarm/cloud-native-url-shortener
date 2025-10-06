provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "logs" {
  bucket = "url-shortener-logs-${random_id.bucket_id.hex}"
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

resource "aws_db_instance" "postgres" {
  identifier         = "url-shortener-db"
  engine             = "postgres"
  instance_class     = "db.t3.micro"
  allocated_storage  = 20
  db_name               = "shortener"
  username           = var.db_username
  password           = var.db_password
  publicly_accessible = true
  skip_final_snapshot = true
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
}

resource "aws_security_group" "rds_sg" {
  name        = "rds-access"
  description = "Allow access from Kubernetes cluster"

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Replace with real IP range
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
