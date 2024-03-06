# Use an official Nginx runtime as a parent image
FROM nginx:latest

# Copy the default Nginx configuration to /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80


# Run custom entrypoint script
CMD ["nginx", "-g", "daemon off;"]
