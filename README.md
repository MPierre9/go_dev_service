## Get go module sum
mkdir temp_module
cd temp_module
go mod init temp


go get github.com/aws/aws-lambda-go@v1.40.0
The go.sum file will now contain the checksum information for the package. 
github.com/aws/aws-lambda-go v1.27.0 h1:<sum-value>

go_repository(
    name = "com_github_aws_aws_lambda_go",
    importpath = "github.com/aws/aws-lambda-go",
    sum = "h1:<sum-value>",
    version = "v1.27.0",
)
# go_dev_service
