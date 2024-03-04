# Use an official Nginx runtime as a parent image
FROM nginx:latest

# Copy the default Nginx configuration to /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

# Define environment variable
ENV FLASK_APP flask-app
ENV FLASK_PORT 5000

# Run custom entrypoint script
CMD ["sh", "/etc/nginx/start.sh"]