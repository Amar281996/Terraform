output "instance_public_ip" {
  description = "Public IP of the Nginx server"
  value       = module.nginx_server.instance_public_ip
}

