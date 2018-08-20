module U(){
  w = 20;
  ancho = 20;
  d  = 30;
  union(){
    color([0.55,0.55,0.55])
    difference(){
      union(){
        cylinder(h=w,r1=w*1.5,r2=w*1.5, center=true);
        translate([0,d*0.5,0]) cube([w*3, d ,w], center=true);}
        
      union(){
        cylinder(h=w+2, r1=w*0.5,r2=w*0.5, center=true);
        translate([0,d/2,0]) cube([w , d+1, w+2],center=true);}
      }
        
      color([1,0.2,0.2])
      translate([w,d+w/2,0]) cube(w,center=true);
        
      color([0.2,0.2,1])
      translate([-w,d+w/2,0]) cube(w,center=true);
           
    }
}


module cuerpo(){
    union(){ 
        difference(){
            color([0.5,0.5,0.5])
            sphere(50, $fn=100);
            color([0,0,0])
            translate([0,0,+90]) cube(100 , center=true);}
       color([1,1,1]) difference(){
            translate([0,0,1])scale([0.9,0.9, 0.99]) sphere(51, $fn=100);
            translate([0,0,-13]) cube(105, center=true);}
       
       color([0,0,0])
            translate([0,0,50]) 
            scale([1,1,0.4]) 
            cylinder(h=10, r1=5, r2=5, center=true); //Ojo
            }
 }

module tornillo(){
    color([0.65,0.65,0.65])
    union(){
        translate([0,0,-7.5]) cylinder(h=15, r1=5, r2=5, center=true);
        scale([1.3,1.3,0.7])
        difference(){
            sphere(10,$fn=50, center=true);
            translate([0,0,-10]) cube(20, center=true);
            translate([0,0,10]) scale([1,0.075,0.35]) cube(30, center=true);
            translate([0,0,10]) scale([0.075,1,0.35]) cube(30, center=true);
            }
        
        }
    }


module magnemite(){
    union(){
        cuerpo();
        rotate([0,0,45])translate([0,80,0])rotate([0,15,0])U();
        rotate([0,0,-45])translate([0,80,0])rotate([0,-10,0])U();
        translate([0,65,0]) rotate([-90,0,0]) scale([1.25,1.25,1.25])  tornillo();
        rotate([40,0,140]) translate([0,58,0]) rotate([-90,0,0]) tornillo();
        rotate([40,0,-140]) translate([0,58,0]) rotate([-90,0,0]) tornillo();
        }
}

module magneton(){
    union(){
        translate([0,60,0]) magnemite();
        rotate([0,0,-120]) translate([0,60,0]) rotate([-20,0,0]) magnemite();
        rotate([0,0,120]) translate([0,60,0]) rotate([-20,0,0]) magnemite();
        }
    
    }
magneton();

// U();
//tornillo();