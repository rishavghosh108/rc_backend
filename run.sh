set -e 
export PYTHONDONTWRITEBYTECODE='1'
export FLASK_APP=core/server.py
export verification_token_key='verification'
export otp_verify_header_key='otpverify'

export root_authorization_secret_key="rookdkdkdkd"
export emp_authorization_secret_key="empfhfhfhfh"
export user_authorization_secret_key="usersksksjdj"

export root_authorization_header_key='root_auth'
export emp_authorization_header_key='emp_auth'
export user_authorization_header_key='user_auth'

export forget_token_key='Forget'

# flask db init
flask db stamp heads
flask db migrate -m "Initial migration."
flask db upgrade

# Run server
gunicorn -c gunicorn_config.py core.server:app