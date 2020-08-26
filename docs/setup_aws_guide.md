# Hvordan gjøre klart AWS for høsting

## Motivasjon
For å kunne høste API-navn fra AWS trenger vi følgende informasjon:
1. En access key ID
2. En secret access key
3. Regionen der Gatewayen bor

Brukeren assosiert med denne nøkkelen trenger følgende rettigheter:
```json
{
		"Effect": "Allow",
		"Action": "apigateway:GET",
		"Resource": [
				"arn:aws:apigateway:eu-central-1::/apis",
				"arn:aws:apigateway:eu-central-1::/restapis"
		]
}
```

Om dere bruker Terraform kan dere bruke
[denne](https://github.com/oslokommune/devportal-harvest-poc/blob/master/docs/terraform_iam_config.tf) filen som inspirasjon. Hvis
dere foretrekker webgrensesnitt så beskriver vi hvordan opprette en bruker
via webgrensesnittet [her](#-Via-Webgrensenitt)


## Via Webgrensesnitt
### Lag en policy
1. Gå til AWS sin [IAM](https://console.aws.amazon.com/iam) tjeneste og velg
	 "Policies" i menyen på venstre side.
2. Velg "Create Policy".
3. I "Service" velg tjenesten "API Gateway".
4. I "Actions" søk etter og velg handlingen "GET".
5. I "Resources" velg "Specific" og trykk "Add ARN".
	1. Legg til en ARN med ønsket region og "/apis" som resource path.
	2. Legg til en ARN med ønsket region og "/restapis" som resource path.
6. Velg "Review policy" og legg inn ønsket navn og beskrivelse.

### Lag en bruker
1. Gå til AWS sin [IAM](https://console.aws.amazon.com/iam) tjeneste og velg
	 "Users" i menyen på venstre side.
2. Velg "Add user".
3. Skriv inn et navn, eksempelvis "origo-api-harvester", og huk av for
	 "Programmatic access".
4. Velg "Next: Permissions".
5. Trykk "Attach existing policies directly".
6. Finn og velg policien vi lagde i "Lag en policy".
7. Trykk "Next: Tags".
8. Trykk "Next: Review".
9. Trykk "Create user".
10. Trykk "Download .csv". Denne filen krypteres og sendes til
		developerportal@oslo.kommune.no.

## FAQ
### Kryptering av fil
1. `wget https://raw.githubusercontent.com/oslokommune/devportal-harvest-poc/master/docs/public_key.pgp`
2. `gpg --import public_key.pgp`
3. `gpg --encrypt --sign --armor -r julius.pedersen@byr.oslo.kommune.no new_user_credentials.csv`
4. Det vil nå være en kryptert fil i arbeidsmappen som heter `new_user_credentials.csv.asc`, dette
	er filen som skal sendes til `developerportal@oslo.kommune.no`
