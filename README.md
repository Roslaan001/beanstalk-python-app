# Flask App for AWS Elastic Beanstalk

A lightweight Python Flask starter application configured for deployment on AWS Elastic Beanstalk.

## Project Structure

```text
├── application.py       # Main entry point (EB looks for 'application.py' and 'application' callable)
├── requirements.txt     # Python dependencies
├── Procfile             # Command used by Elastic Beanstalk to run Gunicorn
├── templates/
│   └── index.html       # Landing page HTML
├── .gitignore
└── README.md
```

---

## 1. Local Development

1. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python application.py
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 2. Deploy to AWS Elastic Beanstalk

### Option A: Using AWS Management Console (Zip Upload)

1. Package the project into a zip file (**exclude** any virtual environment or git folders):
   ```bash
   zip -r app.zip application.py requirements.txt Procfile templates/
   ```

2. Open the [AWS Elastic Beanstalk Console](https://console.aws.amazon.com/elasticbeanstalk/).
3. Click **Create application**.
4. Set the platform to **Python** (e.g. Python 3.11 or Python 3.12 on Amazon Linux 2023).
5. Under **Application code**, select **Upload your code** and upload `app.zip`.
6. Click **Create app**.

### Option B: Using EB CLI

1. **Install the EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**:
   ```bash
   eb init -p python-3.11 my-flask-app
   ```

3. **Create the environment & deploy**:
   ```bash
   eb create my-flask-env
   ```

4. **Open in browser**:
   ```bash
   eb open
   ```
