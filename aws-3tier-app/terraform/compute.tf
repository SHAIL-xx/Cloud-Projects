resource "aws_instance" "app_server" {
  ami                    = "ami-1234567890" # Localstack accepts any mock AMI ID string
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.private_1.id
  vpc_security_group_ids = [aws_security_group.app_sg.id]

  tags = {
    Name = "3tier-app-server"
  }
}