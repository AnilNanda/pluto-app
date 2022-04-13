pipeline {
    agent any
    stages{
        stage('clean workspace'){
            steps{
                script{
                    cleanWs()
                }
            }
        }
        stage('checkoutscm'){
            steps{
                git credentialsId: 'github', 
            url: 'https://github.com/AnilNanda/pluto-app',
            branch: 'main'
            }
        }
        stage('Snyk testing') {
      steps {
        echo 'Snyk vulnerability check...'
        snykSecurity(
          snykInstallation: 'SnykLatest',
          snykTokenId: 'snyk'.
          additionalArguments: "--file=requirements.txt --command=python3"
        )
      }
    }
        stage('Package image'){
            steps{
                script{
                docker.build("${params.ECR_REPO_NAME}:${env.BUILD_ID}")
		  sh "echo Docker build completed successfully"
            }
            }
        }
        // stage('Trivy scan image'){
        //     steps{
        //         script{
        //             sh "trivy ${params.ECR_REPO_NAME}:${env.BUILD_ID}"
		//   sh "echo Docker build completed successfully"
        //     }
        //     }
        // }
        stage('Publish Image'){
            steps{
                script{
                    docker.withRegistry("${params.ECR_HOST}","ecr:${params.ECR_REGION}:${ECR_CREDS}"){
		  	docker.image("${params.ECR_REPO_NAME}:${env.BUILD_ID}").push("${params.ECR_REPO_NAME}-${env.BUILD_ID}")
			docker.image("${params.ECR_REPO_NAME}:${env.BUILD_ID}").push("latest")
                    }
                }
        }
    }
    stage('cleanup images'){
        steps{
            script{
                sh "docker system prune -af"
            }
        }
    }
}
}