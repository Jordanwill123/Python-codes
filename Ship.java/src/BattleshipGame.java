
public class BattleshipGame {
    private static final int BOARD_SIZE = 10;
    private static final int NUM_SHIPS = 5;
    private static final int SHIP_LENGTHS[] = { 5, 4, 3, 3, 2 };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Player player1 = new Player(1);
        Player player2 = new Player(2);

        System.out.println("Welcome to Battleship!");

        player1.placeShips(scanner);
        System.out.println("\n" + player1.getName() + " has placed their ships.");

        player2.placeShips(scanner);
        System.out.println("\n" + player2.getName() + " has placed their ships.");

        System.out.println("\nLet's begin!");

        boolean player1Turn = true;
        while (true) {
            Player currentPlayer = player1Turn ? player1 : player2;
            Player opponentPlayer = player1Turn ? player2 : player1;

            System.out.println("\n" + currentPlayer.getName() + ", it's your turn!");
            boolean hit = currentPlayer.attack(scanner, opponentPlayer);
            if (hit) {
                System.out.println("Hit!");
            } else {
                System.out.println("Miss!");
            }

            if (opponentPlayer.allShipsSunk()) {
                System.out.println("\n" + currentPlayer.getName() + " has won!");
                break;
            }

            player1Turn = !player1Turn;
        }

        scanner.close();
    }
}