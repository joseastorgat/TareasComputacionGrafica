module estrella(){
    color([64/255,42/255,99/255])
    union(){        
        for(angle=[0:72:288]){
            rotate([0,0,angle])
            parteestrella();
        }
    }
}

module parteestrella(){
   union(){       
       translate([0,0,3])
       polyhedronestrella();
       linear_extrude(height=6,center=true){
           polygon([[0,0], [30,30], [0,100],[-30,30]]);
           }      
       translate([0,0,-3])
       rotate([0,180,0])
       polyhedronestrella();          
    }
}

module polyhedronestrella(){
    polyhedron(
        points=[ [0,100,0],[-30,30,0],[30,30,0],[0,0,0], // the four points at base
                [0,0,15]],                                 // the apex point 
        faces=[ [0,1,4],[0,2,4],[2,3,4],[3,0,4],              // each triangle side
              [0,1,3],[0,2,3]]                         // two triangles for square base
    );   
 }
     
 module partebase(){
     w = 5; //ancho/2
     h = 8; //height
     ext= 36; //
     ri = 17; 
 
     polyhedron(
         
    points=[ [-w,0,h],[w,0,h],[w, ext, 0],[-w, ext,0], //
             [-2*w, ext*0.4 ,0], [2*w, ext*0.4, 0]  ],  //
    faces=[ [0,1,3],[1,2,3], //
            [0,3,4],[1,2,5]]  //                       
    );
}
     
 module base(){
     union(){
    
         rotate([0,0,22.5])
         union(){
         color([1,0,0])
         translate([0,0,8])
         cylinder(3,18,10,$fn=8); //rubi
         color([1,1,0])
         cylinder(8,19,19,$fn=8); //
         }
         
         color([1,1,0])
         cylinder(8,35,17,$fn=24);
         
         color([1,1,0])
         for(i=[0:45:315]){
            rotate([0,0,i])   
            translate([0,18,0])
            partebase();
         }
    }
}

module starmie(){
      union(){
          estrella();
          translate([0,0,-20])
          rotate([0,0,36]) 
          estrella();
          translate([0,0,13])
          base();
          }
      }  
    
 //translate([0,0,-20])     
starmie();
//color([64/255,42/255,99/255])
//estrella();

//base();
//parteestrella();