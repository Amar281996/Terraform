output "instance_public_ip" {
  description = "Public IP of the Nginx server"
  value       = aws_instance.nginx_server.public_ip
}