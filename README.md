# YouBrand
YouBrand attempts to create an app which replaces product branding and labeling with a personalized list of product details you find interesting. No more arduously looking through ingredients and reduce the affect of companies' marketing on your consumer choice. 

## Examples of items in YouBrand

### Show only the ingredients you're interested in
Protein count, allergy's, meat or dairy

### Show if a big evil company is behind your product:
Nestle, one of the world's largest and most notorious multinational corporations, has a well-documented history of wrongdoing that spans decades. From unethical marketing of infant formula to profiting from stolen water, exploiting child labor in cocoa production, to their audacious claims that water should not be a universal human right, Nestle has consistently raised ethical concerns. The colossal conglomerate often hides behind an array of different brand names, makeing it difficult for consumers to join in boycotts and make ethical decisions on what the consume. 

This repository represents an effort to empower consumers in doing just that. In the future, the scope of this app may expand to encompass other major corporations that engage in unethical practices, but for now we'll just do Nestle. 

Milk Alternatives (Infant Formula Controversy):
[Baby Milk Action - Nestle and the Baby Killer
The Guardian - The Baby Killers](https://www.babymilkaction.org/nestlefree)

Stealing Water:
https://www.theguardian.com/global/2018/oct/04/ontario-six-nations-nestle-running-water

Child Labor in Cocoa Production:
https://www.bbc.com/news/world-africa-18644870

Claiming Water Shouldn't Be a Universal Right:
https://aarhusclearinghouse.unece.org/news/nestle-ceo-water-not-a-human-right-should-be-privatized
https://www.youtube.com/watch?v=mTnJTyeAUA8






The app will consist of a few different parts:
1. Import a picture from camera or files, locate the barcode and read the manufacturer code. 
2. Make an API call to [https://barcodeapi.org/index.html#auto](https://www.barcodelookup.com/)
3. Look up the manufacturer in a table which lists all nestle sub brands.
4. Display to the user if the product is made by nestle and tell them to buy something else.

