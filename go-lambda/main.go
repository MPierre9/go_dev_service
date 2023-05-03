package main

import (
	"context"
	"fmt"
	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"net/http"
	// "strings"
)

func handler(ctx context.Context, request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {

	fmt.Sprintf("Hello World")
	return events.APIGatewayProxyResponse{
		StatusCode: http.StatusOK,
		Body:       fmt.Sprintf("Hello World"),
	}, nil


	// issueKey := request.QueryStringParameters["issueKey"]
	// if issueKey == "" {
	// 	return events.APIGatewayProxyResponse{
	// 		StatusCode: http.StatusBadRequest,
	// 		Body: "issueKey query parameter is required",
	// 	}, nil
	// }

	// jiraURL := fmt.Sprintf("https://your-domain.atlassian.net/rest/api/3/issue/%s", issueKey)

	// req, err := http.NewRequest("GET", jiraURL, nil)
	// if err != nil {
	// 	return events.APIGatewayProxyResponse{
	// 		StatusCode: http.StatusInternalServerError,
	// 		Body:       err.Error(),
	// 	}, nil
	// }

	// req.Header.Add("Accept", "application/json")
	// req.SetBasicAuth("your-email", "your-api-token")

	// client := &http.Client{}
	// resp, err := client.Do(req)
	// if err != nil {
	// 	return events.APIGatewayProxyResponse{
	// 		StatusCode: http.StatusInternalServerError,
	// 		Body:       err.Error(),
	// 	}, nil
	// }
	// defer resp.Body.Close()

	// return events.APIGatewayProxyResponse{
	// 	StatusCode: resp.StatusCode,
	// 	Body:       strings.TrimSpace(string(resp.Body)),
	// }, nil
}

func main() {
	lambda.Start(handler)
}
