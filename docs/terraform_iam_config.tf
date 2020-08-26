data "aws_iam_user" "origo_api_harvester" {
  user_name = "origo-api-harvester"
}

resource "aws_iam_user_policy_attachment" "origo_api_harvester_policy" {
  user = data.aws_iam_user.origo_api_harvester.user_name

  policy_arn = aws_iam_policy.origo_api_harvester_policy.arn
}

resource "aws_iam_policy" "origo_api_harvester_policy" {
  name   = "origo-api-harvester"
  policy = data.aws_iam_policy_document.origo_api_harvester_policy.json

  description = "Provide API Gateway access to the Origo API Harvester user"
}

data "aws_iam_policy_document" "origo_api_harvester_policy" {
  statement {
    actions = ["apigateway:GET"]
    resources = [
      "arn:aws:apigateway:${data.aws_region.this.name}::/restapis",
      "arn:aws:apigateway:${data.aws_region.this.name}::/apis"
    ]
  }
}
