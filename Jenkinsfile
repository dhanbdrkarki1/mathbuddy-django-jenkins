
pipeline {
    agent any

    environment {
        SONAR_HOME = tool 'sonar-scanner'
        SONAR_PROJECT_KEY = 'mathbuddy-django'
        
        //django superuser
        DJANGO_ADMIN_USERNAME = 'admin'
        DJANGO_ADMIN_EMAIL = 'admin@gmail.com'
        DJANGO_ADMIN_PASSWORD = 'P@ssword0'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/dhanbdrkarki1/mathbuddy-django-jenkins.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'sudo apt-get update -y'
                sh 'sudo apt-get install -y python3-pip python3-venv python3-dev'
                sh 'python3 -m venv venv'
                withEnv(['PATH+VENVS=venv/bin']) {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        
        
        stage('Sonarqube analysis') {
            steps {
                script {
                    withSonarQubeEnv('sonarqube') {
                        sh """
                        ${SONAR_HOME}/bin/sonar-scanner \
                        -Dsonar.projectName=${SONAR_PROJECT_KEY} \
                        -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                        -Dsonar.java.binaries=. \
                        -Dsonar.sources=. \
                        -Dsonar.exclusions=venv,requirements.txt,tests,migrations,asgi.py,wsgi.py,manage.py \
                        -Dsonar.python.version=3
                        """
                    }
                }
            }
            
        }
        
        stage("OWASP SCAN"){
        	steps{
        		dependencyCheck additionalArguments: '--scan ./', odcInstallation:'owasp-dependency-check'
        		dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
        	}
        }
        stage('Build & Push Docker Image'){
            steps{
                   script{
                       withDockerRegistry(credentialsId: 'docker', toolName: 'docker') {
                            sh "docker build -t mathbuddy:latest ."
                            sh "docker tag mathbuddy:latest dhan007/mathbuddy:latest"
                            sh "docker push dhan007/mathbuddy:latest"
                        }
                   }
                }
            }
        stage('Deploy'){
            steps{
                   script{
                       withDockerRegistry(credentialsId: 'docker', toolName: 'docker') {
                            sh "docker compose up -d"
                            //since custom user is used, it needs to created first hence base app should be defined.
                            sh 'docker compose exec mathbuddy-web python /code/manage.py makemigrations base'
                            sh 'docker compose exec mathbuddy-web python /code/manage.py migrate'
                            
                            sh 'docker compose exec mathbuddy-web python /code/manage.py collectstatic --noinput'
                            
                            
                        }
                   }
                }
            }
        stage('Create Superuser'){
            steps{
                script{
                    //creating super user non-interactively
            sh "echo 'from base.models import User; User.objects.create_superuser(username=\"$DJANGO_ADMIN_USERNAME\", email=\"$DJANGO_ADMIN_EMAIL\", password=\"$DJANGO_ADMIN_PASSWORD\")' | docker compose exec -T mathbuddy-web python /code/manage.py shell"
                }
            }
        }
        
    }
}