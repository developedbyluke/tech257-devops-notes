provider "aws" {
  region = "eu-west-1"
}

resource "aws_security_group" "tech257-lukeh-sg" {
  name = "tech257-lukeh-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "tech257-lukeh-terraform-app" {
  tags = {
    Name = "tech257-lukeh-terraform-app"
  }
  ami                         = var.ami_id
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  key_name                    = "tech257"
  vpc_security_group_ids      = [aws_security_group.tech257-lukeh-sg.id]
}
