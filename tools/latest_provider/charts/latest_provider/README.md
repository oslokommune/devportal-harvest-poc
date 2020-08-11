# simple-chart starter

Mal for et enkelt Helm chart, med ingress.

I dette eksemplet kjører vi opp en enkel, men fungerende nginx-server.

Med untak av mounting av volumes i [deployment.yaml](./templates/deployment.yaml),
så er imidlertid det meste av chartet relativt generisk, og styres av verdiene som settes i 
[values.yaml](./values.yaml).

Chartet er ment som et utgangspunkt for å få opp andre enkle applikasjoner. Man må
regne med å gjøre endringer for å tilpasse chartet til sitt behov.