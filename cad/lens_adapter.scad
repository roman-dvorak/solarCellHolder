$fn=150;

difference(){
    union(){    
        cylinder(h=1, d=67);
        cylinder(h=22, d=61);
    }
    
    cylinder(h=30, d=55);
    translate([0,0,11])cylinder(h=30, d=58.7);
}