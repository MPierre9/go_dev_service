.PHONY: build test package deploy

build:
	bazel build //go-lambda

test:
	bazel test //...

package:
	zip go_lambda.zip bazel-bin/go-lambda
	aws s3 cp go_lambda.zip s3://mpierre-lambdas-821777302053/go_lambda/go_lambda.zip


# deploy: package
# 	aws cloudformation package \
# 		--template-file cfn/template.py \
# 		--output-template-file cfn/packaged.yaml \
# 		--s3-bucket your-s3-bucket-name \
# 		--s3-prefix your-s3-prefix
# 	aws cloudformation deploy \
# 		--template
