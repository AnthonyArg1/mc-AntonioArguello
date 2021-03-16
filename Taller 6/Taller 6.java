double angulo;
		double radian;
		double cos;
		double form = 0;
		System.out.print("ingrese el angulo: ");
		angulo = leer.nextDouble();
		radian =angulo*Math.PI/180;

		cos =Math.cos(radian);
		
		System.out.println("angulo radian "+ radian);
		double es =(radian*Math.pow(10, -8))*100;
		System.out.println("  valor esperado "+ radian);
		double ex=100;

		 for (int i = 0; i < 8; i+=2) {
			 int signo =1;
			form += signo*Math.pow(radian, i)/factorial(i);
			signo *= -1;
		}

		
	
System.out.println("forma aproximada:"+form);
double error =((form-es)/form)*100;
System.out.print("la probalidad de error es :"+error);
}

	 static double factorial (int interaciones) {
			double rta=1;
			for (int i = 1; i <= 8; i++) {
				rta*=i;
			}
			return rta;
		}