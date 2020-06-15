# image-recognition

## Código

Localizado na pasta image-recognition/code

## Templates

Localizados na image-recognition/

## Comandos:

- **sam init** - Inicia a aplicação SAM e define as configurações

- **sam build --guided -t template.yaml** - Faz o build da aplicação e configura os recursos na primeira vez

- **sam local invoke ImageCheckRecognitionFunction --event events/teste_mulher.json** - Faz a chamada local da função para testar com uma foto de mulher

- **sam local invoke ImageCheckRecognitionFunction --event events/teste_homem.json** - Faz a chamada local da função para testar com uma foto de homem

- **sam deploy** - Faz o deploy da aplicação e devolve o endereço da API Gateway

## Links

- [Analise de uma aplicação SQS x KINESIS](https://eng.lifion.com/aws-lambda-triggers-kinesis-vs-sqs-1a1c78a86600)

- [Detalhando mais o lambda](https://github.com/epsagon/lambda-internals)

- [Eventbridge exemplos](https://www.serverless.com/blog/eventbridge-use-cases-and-tutorial/)

- [Um exemplo de preços no Lambda](https://blog.binaris.com/lambda-pricing-pitfalls/)

- [10 boas práticas serverless](https://www.datree.io/resources/serverless-best-practices)

- [Cold start in AWS Lambda](https://mikhail.io/serverless/coldstarts/aws/)

- [Coisas que devem ser medidas em funções lambdas](https://www.bluematador.com/blog/top-7-aws-lambda-metrics-to-monitor)

- [Entendendo preços do S3](https://www.sumologic.com/insight/s3-cost-optimization/)

- [Tudo sobre DynamoDB](https://www.serverless.com/dynamodb/)

- [Polícia de Oregon usa AWS Rekognition](https://www.washingtonpost.com/technology/2019/04/30/amazons-facial-recognition-technology-is-supercharging-local-police/)

- [Treinamento AWS Serverless](https://www.aws.training/Details/eLearning?id=42594)

- [Boas ferramentas para monitoramento](https://www.serverless.com/blog/best-tools-serverless-observability/)