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
				"arn:aws:apigateway:<region hvor gateway kjører>::/apis",
				"arn:aws:apigateway:<region hvor gateway kjører>::/restapis"
		]
}
```

Om dere bruker Terraform kan dere bruke
[denne](https://github.com/oslokommune/devportal-harvest-poc/blob/master/docs/terraform_iam_config.tf) filen som inspirasjon. Hvis
dere foretrekker webgrensesnitt så beskriver vi hvordan opprette en bruker
via webgrensesnittet [her](#via-webgrensenitt)


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

### Oppsett av bruker
Litt avhengig av organisasjonsstrukturen deres kan en bruker enten lages eller
bestilles. Hvis du har rettigheter til å lage en bruker kan
[disse](#lag-en-bruker) stegene følges. Hvis du derimot må bestille en bruker,
se [her](#jeg-får-ikke-lov-til-å-opprette-en-bruker).

#### Lag en bruker
1. Gå til AWS sin [IAM](https://console.aws.amazon.com/iam) tjeneste og velg
	 "Users" i menyen på venstre side.
2. Velg "Add user".
3. Skriv inn et navn, eksempelvis "origo-api-harvester", og huk av for
	 "Programmatic access".
4. Velg "Next: Permissions" og følg stegene i [Konfigurer rettigheter](#konfigurer-rettigheter)

#### Jeg har fått tilegnet en bruker
1. Gå til AWS sin [IAM](https://console.aws.amazon.com/iam) tjeneste og velg
	 "Users" i menyen på venstre side.
2. Velg den tilegnede brukeren i listen.
3. Trykk "Add permissions" og følg stegene i [Konfigurer rettigheter](#konfigurer-rettigheter)

## Konfigurer rettigheter
1. Trykk "Attach existing policies directly".
2. Finn og velg policien vi lagde i [Lag en policy](#lag-en-policy).
3. Trykk "Next: Tags".
4. Trykk "Next: Review".
5. Trykk "Create user".
6. Trykk "Download .csv". Denne filen [krypteres](#hvordan-krypterer-jeg-en-fil) og sendes til
		developerportal@oslo.kommune.no.

## FAQ
### Hvordan krypterer jeg en fil
1. `wget https://raw.githubusercontent.com/oslokommune/devportal-harvest-poc/master/docs/public_key.pgp`
2. `gpg --import public_key.pgp`
3. `gpg --encrypt --sign --armor -r julius.pedersen@byr.oslo.kommune.no new_user_credentials.csv`
4. Det vil nå være en kryptert fil i arbeidsmappen som heter `new_user_credentials.csv.asc`, dette
	er filen som skal sendes til `developerportal@oslo.kommune.no`

### Jeg får ikke lov til å opprette en bruker
Hvis det er UKE som håndterer opprettelse av brukere for dere, så må det
bestilles en bruker i Kompass. For å bestille bruker trenger UKE å vite
følgende:
* Navn på ny bruker
* Hvilken AWS konto brukeren skal knyttes opp mot

Etter brukeren har blitt opprettet kan stegene [her](#jeg-har-fått-tilegnet-en-bruker) følges.
