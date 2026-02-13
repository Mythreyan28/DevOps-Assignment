output "alb_dns" {
  value = aws_lb.main.dns_name
}

output "backend_url" {
  value = "http://${aws_lb.main.dns_name}/api/health"
}

output "frontend_url" {
  value = "http://${aws_lb.main.dns_name}"
}

