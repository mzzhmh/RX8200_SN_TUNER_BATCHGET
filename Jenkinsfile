node
{
        stage('Check Out') {
	    checkout scm
        }
	stage('List files') {
	    sh "ls -lrt"
        }
        stage('Deploy') {
            sh "rsync -av ./* /opt/RX8200SNGET/"
        }
        stage('Run report'){
	    sh "/opt/RX8200SNGET/getsnDaily.sh"
	}
}

