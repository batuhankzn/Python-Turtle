import turtle

# Tuşları kontrol etmek için turtle ekranı oluştur
wn = turtle.Screen()
wn.title("Turtle Yönlendirme")
wn.bgcolor("white")

# Turtle nesnesini oluştur
player = turtle.Turtle()
player.shape("turtle")

# Turtle'ı ileriye doğru hareket ettirmek için bir fonksiyon
def ileri():
    player.forward(10)

# Turtle'ı sola çevirmek için bir fonksiyon
def sola():
    player.left(90)

# Turtle'ı geriye doğru hareket ettirmek için bir fonksiyon
def geri():
    player.backward(10)

# Turtle'ı sağa çevirmek için bir fonksiyon
def saga():
    player.right(90)

# Tuşları işlemek için tuş bağlantıları ayarla
wn.listen()
wn.onkey(ileri, "w")
wn.onkey(sola, "a")
wn.onkey(geri, "s")
wn.onkey(saga, "d")

# Sonsuz döngüde kal
wn.mainloop()
