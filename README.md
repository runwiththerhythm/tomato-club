## 🚀 Deployment

The Heritage Tomato Club is deployed to a live VPS environment using **Nginx**, **Gunicorn**, **PostgreSQL**, and **Let’s Encrypt SSL**.

### 🔗 Live Site

**[https://tomatoes.cassiterite.digital](https://tomatoes.cassiterite.digital)**

### ⚙️ Deployment Summary

The project was deployed using the following steps:

1. SSH into the VPS.
2. Clone the GitHub repository into the project directory.
3. Create and activate a Python virtual environment.
4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
6. Build Tailwind CSS and collect static files:

   ```bash
   python manage.py tailwind build
   python manage.py collectstatic --noinput
   ```
7. Configure **Gunicorn** as the application server using a systemd service.
8. Configure **Nginx** as a reverse proxy to Gunicorn and enable HTTPS via Let’s Encrypt.
9. Reload all services to complete deployment.

### 🔄 Updating the Live Server

To deploy updates:

```bash
git pull
python manage.py migrate
python manage.py tailwind build
python manage.py collectstatic --noinput
sudo systemctl restart <app-service>
```
