from troposphere import Template, Ref, GetAtt, Join
from troposphere.apigateway import RestApi, Resource, Method, Integration
from troposphere.awslambda import Function, Code, Environment, Permission
from troposphere.iam import Role, Policy

template = Template()

# API Gateway
api_gateway = template.add_resource(
    RestApi(
        "ApiGateway",
        Name="JiraIntegrationApi",
    )
)

api_gateway_resource = template.add_resource(
    Resource(
        "ApiGatewayResource",
        RestApiId=Ref(api_gateway),
        PathPart="trigger",
        ParentId=GetAtt(api_gateway, "RootResourceId"),
    )
)

api_gateway_method = template.add_resource(
    Method(
        "ApiGatewayMethod",
        RestApiId=Ref(api_gateway),
        ResourceId=Ref(api_gateway_resource),
        HttpMethod="GET",
        AuthorizationType="NONE",
    )
)

# Lambda Function
lambda_role = template.add_resource(
    Role(
        "LambdaRole",
        AssumeRolePolicyDocument={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": ["lambda.amazonaws.com"]},
                    "Action": ["sts:AssumeRole"],
                }
            ],
        },
        Policies=[
            Policy(
                PolicyName="AllowJiraAPIAccess",
                PolicyDocument={
                    "Version": "2012-10-17",
                    "Statement": [
                        # Add necessary permissions for your Lambda function to access the Jira API
                    ],
                },
            )
        ],
    )
)

lambda_function = template.add_resource(
    Function(
        "LambdaFunction",
        Code=Code(S3Bucket="your-s3-bucket", S3Key="your-s3-prefix/lambda.zip"),
        Handler="main",
        Role=GetAtt(lambda_role, "Arn"),
        Runtime="go1.x",
        Environment=Environment(Variables={"JIRA_API_KEY": "your-jira-api-key"}),
        Timeout=10,
    )
)

# API Gateway Integration with Lambda
lambda_permission = template.add_resource(
    Permission(
        "LambdaPermission",
        Action="lambda:InvokeFunction",
        FunctionName=Ref(lambda_function),
        Principal="apigateway.amazonaws.com",
        SourceArn=Join("", [
            "arn:aws:execute-api:",
            Ref("AWS::Region"),
            ":",
            Ref("AWS::AccountId"),
            ":",
            Ref(api_gateway),
            "/*/GET/trigger",
        ]),
    )
)

api_gateway_integration = template.add_resource(
    Integration(
        "ApiGatewayIntegration",
        RestApiId=Ref(api_gateway),
        ResourceId=Ref(api_gateway_resource),
        HttpMethod=Ref(api_gateway_method),
        Type="AWS_PROXY",
        IntegrationHttpMethod="POST",
        Uri=Join("", [
            "arn:aws:apigateway:",
            Ref("AWS::Region"),
            ":lambda:path/2015-03-31/functions/",
            GetAtt(lambda_function, "Arn"),
            "/invocations",
        ]),
    )
)

# Generate the CloudFormation template
print(template.to_yaml())
