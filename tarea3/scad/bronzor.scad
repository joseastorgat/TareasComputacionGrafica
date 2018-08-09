function cat(L1, L2) = [for(L=[L1, L2], a=L) a];
module cuerpo(re,eg,resf){
    union(){
        color([61/255,171/255,188/255]) cylinder(h = eg, r1 = re, r2=re, center = true);
        color([45/255,124/255,139/255])
        for(i=[30:60:330]){
            bola(posicion=[cos(i)*re, sin(i)*re,0], radio=resf);
        }
     }
 }

module bola(posicion=[0,0,0], radio = 1){
    translate(posicion)
    sphere(radio, center=true);
}

module cara(ri,ep,rnariz, re){
    
    union(){
        
        color(c=[45/255,124/255,139/255]) cylinder(h = ep , r1= ri, r2=ri, center = true);
        
        color([61/255,171/255,188/255])
        
        translate([0,0,ep/2])
        
        difference(){
            bola([0,0,0], rnariz);
            translate([0,0,-rnariz]) cube(2*rnariz, center=true);}
          
        translate([re/2.5,0,10])
        ojo(re);
        translate([-re/2.5,0,10])
        ojo(re);
        
        translate([0,0,ep/2])
        color([0,0,0])
        union(){
        difference(){
            circle(r=re/2.45, h=re/100, center=true);
            circle(r=re/2.55, center=true);   
            //cylinder(r1=re/2.4, r2=re/2.4, h=re/100, center=true);
            //cylinder(r1=re/2.6, r2=re/2.6, h=re/100, center=true);
            
        }        
       scale([1,1,0.2])
       for(i=[60,120,240,300]){
            bola(posicion=[cos(i)*(re/2.5+ re/60), sin(i)*(re/2.5 + re/60),0], radio=re/15);
        }
        }
    
    
    }
}
module ojo(re){
    
    union(){
        color([1,1,1])
        scale([1,2,1])
        cylinder(h=re/10, r1=re/10 ,r2=re/10, center=true);
        color([0,0,0])
        scale([1,2.5,1])
        cylinder(h=re/10, r1=re/25, r2= re/25, center=true);
    }
}

module espalda(ep){
      
    
    color([60/255,140/255,180/255]) 
    translate([0,18,-ep/2])
    union(){
          rama();
        translate([-30,-10,0])
          rotate([0,0,65])
          scale([0.5,0.5,0.5])
          rama();
         
        translate([30,-10,0])
          rotate([0,0,-65])
          scale([0.5,0.5,0.5])
          rama();  

        translate([-30,-40,0])
          rotate([0,0,65])
          scale([0.5,0.5,0.5])
          rama();
         
        translate([30,-40,0])
          rotate([0,0,-65])
          scale([0.5,0.5,0.5])
          rama();            
          }
    
    }

module hoja(){
    c = 0.40;
    t = 0.65;
      coords1= [for( x=[0:0.01:c/4])[ 100*(t*c/0.2)*(0.2969*sqrt(x/c)-0.1260*(x/c)-0.3516*pow((x/c),2)+0.2843*pow((x/c),3) - 0.1015*pow((x/c),4) ),(100*x) ]];    
     
      coords2= [for( x=[c/4: 0.05: c])[ 100*(t*c/0.2)*(0.2969*sqrt(x/c)-0.1260*(x/c)-0.3516*pow((x/c),2)+0.2843*pow((x/c),3) - 0.1015*pow((x/c),4) ),(100*x) ]];

     coords3= [for( x=[c:-0.05:c/4])[ -100*(t*c/0.2)*(0.2969*sqrt(x/c)-0.1260*(x/c)-0.3516*pow((x/c),2)+0.2843*pow((x/c),3) - 0.1015*pow((x/c),4)) ,(100*x) ]];
    
     coords4= [for( x=[c/4:-0.02:0])[ -100*(t*c/0.2)*(0.2969*sqrt(x/c)-0.1260*(x/c)-0.3516*pow((x/c),2)+0.2843*pow((x/c),3) - 0.1015*pow((x/c),4) ),(100*x) ]];    
    coords = cat(coords1,cat(coords2,cat(coords3, coords4)));
    polygon(coords); 
}

module rama(){
    
    linear_extrude(height=2, center=true){
        union(){
            hoja();
            polygon([[2,5],[-2,5],[-6,-70],[6,-70]]);
            }
        
        
        }}
module bronzor(){
    re = 100;        // Radio Externo
    ri = re * (2/3);  // radio Interno
    eg = re /5;     // espesor cilindro grande 
    ep = eg * 1.4;  // espesor cilindro pequeño
    resf = re/5;     // radio de pelotas
    rnariz = resf;   // 

    union(){
        
        cuerpo(re,eg,resf);
        cara(ri,ep,rnariz,re);
        espalda(ep);
    } 
}

bronzor();



//module rama(){
//    
//    difference(){
//        translate([0,0,-0])
//        rotate([0,90,0])
//        scale([0.5,1,1])
//        cylinder(r1=30,r2=30,h=55,center=false);
//    
//    difference(){
//    
//        translate([29,0,0])
//        
//        scale([1,1,0.5])
//        cube(60,center=true);
//        linear_extrude(height=50, center=true){
//        hoja();}
//        }
//    }
//    
//}
