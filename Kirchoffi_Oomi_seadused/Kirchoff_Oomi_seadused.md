
# Kirchoffi ja Oomi seaduste ülesanne


![Skeem](pildid/skeem.png)

Antud skeemis on lihtne ahel, kus saame rakendada nii Oomi kui ka Kirchoff'i seaduseid. *V<sub>1</sub>* näitel tähistab pingelangust takistuses *R<sub>1</sub>* samamoodi kui *I<sub>1</sub>* tähistab voolutugevust mis läheb selle takistuse läbi.

Sinu ülesanne on koostada esimese skeemi ahel.
Esimene variant oleks kõik takistused sama väärtusega:

*R<sub>1</sub>* = *R<sub>2</sub>* = *R<sub>3</sub>* = 220 Ω

See oleks variant, mis on pildi peal.

![Skeem 1](pildid/220_Kirchoff_Oomi_schem.png)

Kuna *R<sub>2</sub>* ja *R<sub>3</sub>* on rööpühenduses:

1/R<sub>23</sub> = 1/*R<sub>2</sub>* + 1/*R<sub>3</sub>*

R<sub>23</sub> = (*R<sub>2</sub>*+*R<sub>3</sub>*)/*R<sub>2</sub>***R<sub>3</sub>*

Eelmise skeemi saab lihtsustada nii:

![Skeem 2](pildid/220_Kirchoff_Oomi_2_schem.png)

Kuna *R<sub>1</sub>* ja R<sub>23</sub> on jadaühenduses:

R<sub>kokku</sub> = *R<sub>1</sub>* + R<sub>23</sub>

Eelmise skeem saab lihtsustada, et jääks nii:

![Skeem 3](pildid/220_Kirchoff_Oomi_3_schem.png)

Mõõda, mis on pingete, takistuste ja voolutugevuse väärtused.

*V<sub>1</sub>*, *R<sub>1</sub>*, *I<sub>1</sub>*

*V<sub>2</sub>*, *R<sub>2</sub>*, *I<sub>2</sub>*

*V<sub>3</sub>*, *R<sub>3</sub>*, *I<sub>3</sub>*

## Kirchoff'i seadused
Nende mõõtmistega pead tõestama, et:

### (Kirchoff'i esimene seadus)

*I<sub>1</sub>* = *I<sub>2</sub>* + *I<sub>3</sub>*
 
### (Kirchoff'i teine seadus)

V = *V<sub>1</sub>* + *V<sub>2</sub>*

V = *V<sub>1</sub>* + *V<sub>3</sub>* 
 


## Teine variant 

Kui sa oled selle juba ära teinud võid proovida teiste takistuste väärtuste võrdlemist. Nt:

*R<sub>1</sub>* = *R<sub>2</sub>* = 220 Ω

*R<sub>3</sub>* = 10 kΩ


## Kuidas kasutada multimeetrit?

Palun loe hoolikalt järgmist artiklit, kus on seletatud kuidas sa võid mõõta pinge, takistus kui ka voolutugevus multimeetri abiga:

[Link artiklisse](https://www.metshein.com/unit/arduino-multimeetri-kasutamine/)