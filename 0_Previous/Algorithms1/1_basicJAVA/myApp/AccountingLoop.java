package myApp;


public class AccountingLoop {
    public static void main(String[] args) { 
        double valueOfSupply = Double.parseDouble(args[0]); 
        double VATRate = 0.1;
        double expenseRate = 0.3;
        double VAT = valueOfSupply * VATRate;
        double total = valueOfSupply + VAT;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;

        
        System.out.println("Value of Supply: "+ valueOfSupply);
        System.out.println("VAT: "+VAT);
        System.out.println("Total: "+total);
        System.out.println("Expense: "+expense);
        System.out.println("Income: "+income);

        double[] DividendRates = new double[3];
        DividendRates[0] = 0.5;
        DividendRates[1] = 0.3;
        DividendRates[2] = 0.2;

        int i = 0;
        while(i<DividendRates.length){
            System.out.println("Dividend_"+i+":"+(income * DividendRates[i]));
            i = i+1;
        }
    }
}
