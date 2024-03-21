#!/usr/bin/python
from flask import Flask, jsonify
import docker

app = Flask(__name__)

@app.route('/containers', methods=['GET'])
def get_containers():
    # Create a Docker client
    client = docker.from_env()

    # Get a list of running containers
    containers = client.containers.list()

    # Extract relevant information from each container
    container_info = []
    for container in containers:
        container_info.append({
            'id': container.id,
            'name': container.name,
            'image': container.image.tags[0],
            'status': container.status,
            'ports': container.ports,
        })

    # Return the list of container information as JSON
    return jsonify({'containers': container_info})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
