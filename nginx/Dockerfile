# Use an official Nginx runtime as a parent image
FROM nginx:latest

# Copy the default Nginx configuration to /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
COPY . .


# Run custom entrypoint script
CMD ["nginx", "-g", "daemon off;"]
