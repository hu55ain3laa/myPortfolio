"""
Production settings for the portfolio application.
"""

# Set this to True in production
USE_HTTPS = True

# Domain for the application
DOMAIN = "www.hu55ain3laa.site"

# Force all resources to be loaded over HTTPS
# This is needed for deployment on platforms that don't support middleware well
FORCE_HTTPS_RESOURCES = True 