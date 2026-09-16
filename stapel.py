import java.util.ArrayList;
import java.util.Collections;

public class Stapel {

    private ArrayList<Karte> karten;

    // Erstellt einen neuen Stapel
    public Stapel() {
        karten = new ArrayList<>();
        erstelleStapel();
        mischen();
    }

    // UNO-Karten erstellen
    private void erstelleStapel() {
        String[] farben = {"Rot", "Gelb", "Grün", "Blau"};

        for (String farbe : farben) {
            // 0 gibt es einmal
            karten.add(new Karte(farbe, 0));

            // Zahlen 1-9 gibt es zweimal
            for (int i = 1; i <= 9; i++) {
                karten.add(new Karte(farbe, i));
                karten.add(new Karte(farbe, i));
            }
        }
    }

    // Karten mischen
    public void mischen() {
        Collections.shuffle(karten);
    }

    // Oberste Karte ziehen
    public Karte ziehen() {
        if (karten.isEmpty()) {
            return null;
        }

        return karten.remove(karten.size() - 1);
    }

    // Anzahl der Karten im Stapel
    public int anzahlKarten() {
        return karten.size();
    }

    // Prüfen, ob der Stapel leer ist
    public boolean istLeer() {
        return karten.isEmpty();
    }
}