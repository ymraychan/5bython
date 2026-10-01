# v1.0.0 (indev)

## September 26, 2026
* Fix bug where on the very first frame of loading a level objects start at (0, 0)
* Fix clipping into a block
* Add restart key functionality
* Remove guard clause for negative weight due to nonsensicality
* Add restart timer
* Add jump, left, right. Need to fix jumping and moving simultanously.

## September 24, 2026
* Finish level select
* Level select screens are no longer classes
* Objects do stop when colliding with a block but remains clipped in
* Remove guard clause for entity missing torsomat

## September 23, 2026
* Add level select buttons

## September 12, 2026
* Add menu
* Add level select, not complete

## September 2, 2026
* Add start screen, cannot progress past. Also commented out gravity.

## August 27, 2026
* Implement movement and gravity

## August 25, 2026
* Fix door light

## August 24, 2026
* Add tx, ty and fix door. Still need to door light

## August 21, 2026
* Fix box crash issues
* Add javascript file for reading purposes

## August 16, 2026
* Add borders

## August 3, 2026
* Wrap levels in level class

## July 28, 2026
* Implement entity loading

## July 24, 2026
* Fix bug with animated tiles and fix frame drops

## July 22, 2026
* Port everything to pygame instead of pygame zero

## July 20, 2026
* Fix level loading