
Before you begin, ensure that you have Docker and Docker Compose installed on your system.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/amitaiturkel/calc-server-arch-docker-compose.git
   cd calc-server-arch-docker-compose
   ```

2. **Build Docker Images:**

   Build the Docker images for all services:

   ```bash
   docker-compose build
   ```

3. **Run Containers:**

   Start all four containers using Docker Compose:

   ```bash
   docker-compose up
   ```

   The NATS server will be accessible on port 4222, and the FastAPI server will be accessible on port 8000.

4. **Access Services:**

   - Calculator Server: Access the calculator server at `http://localhost:8000` or the appropriate IP address.
   - NATS Server: The NATS server is available at `localhost:4222`.

5. **Client Application:**

   To interact with the client application, open a new terminal window and run the following command:

   ```bash
   docker-compose exec client bash
   ```

   This will open a Bash shell inside the client container. You can then run the client application or provide any required input.

6. **Cleanup:**

   When you're done, you can stop and remove the containers by running the following command in the project directory:

   ```bash
   docker-compose down
   ```

   This will stop and remove the containers but will retain the Docker images for future use.

