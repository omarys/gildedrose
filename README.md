# Gilded Rose Requirements Specification

## Basic Requirements

* All items have a SellIn value which denotes the number of days we have to sell the item
* All items have a Quality value which denotes how valuable the item is
  + The Quality of an item is never negative
  + The Quality of an item is never more than 50
  + Once the sell by date has passed, Quality degrades twice as fast
  + "Aged Brie" actually increases in Quality the older it gets
  + "Sulfuras" always has a value of 80 because it is *Legendary*
  + "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    - Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    - Quality drops to 0 after the concert
  + "Conjured" items degrade in Quality twice as fast as normal items
* At the end of each day our system lowers both values for every item

### Notes

* Make changes to the UpdateQuality method
* Make the UpdateQuality method and Items property static 
* Do not alter the Item class or Items property
