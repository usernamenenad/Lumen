# Komforno predviđanje

Suštinski **nevažno od modela mašinskog učenja**, samo jedna tehnika primjene *datih*. Dakle, možemo koristiti bilo koji model mašinskog učenja, ali ćemo primjeniti *statističke* metode koje govore u kolikom *rasponu* se nalazi *target* nakon unijetih *feature*-a.
**Glavna ideja** jeste da pokušamo učiti iz *grešaka* modela. 
## Primjer

Imamo *trening dataset* $$(x_0, y_0), (x_1, y_1),...,(x_n, y_n)$$
i jednu *testnu tačku* $$(x_{n+1}, ?)$$
Za testnu tačku "*nemamo vrijednost*" (suštinski, mi **znamo** ali je ne dajemo modelu), te ćemo **pretpostaviti** da ona ima vrijednost $y$. 
Fitujmo naš model $C(X)$ koristeći pretpostavljenu tačku $(x_{n+1}, y)$
Sledeći korak je *dobijanje reziduala*, odnosno grešaka predikcije našeg modela u odnosu na stvarnu vrijednost $$e_i = y_i - C(x_i), i \in [0, n+1]$$
Naravno, u reziduale uključujemo i *grešku testne tačke*. Time možemo dobiti *probabilističku distribuciju reziduala* gdje možemo posmatrati koliko često se konkretna greška pojavila.
