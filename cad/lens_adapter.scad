$fn=150;

difference(){
    union(){
        cylinder(h=1.2, d=72);
        cylinder(h=15, d=63);
        cylinder(h=22, d=60);
    }

    cylinder(h=30, d=55-10);
    translate([0,0,1]) cylinder(h=30, d=55);
    translate([0,0,11])cylinder(h=30, d=58.7);
}
