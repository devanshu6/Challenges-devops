# Getting the DNS of load balancer
output "lb_dns_name" {
  description = "The DNS name of the load balancer"
  value       = aws_lb.external-alb.dns_name
}
#storing database password as sensitive parameter
output "db_password" {
  value = aws_db_instance.db.password
  description = "The password for logging into the database"
  sensitive = true
}
