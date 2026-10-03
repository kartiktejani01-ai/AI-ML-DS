story = """
The *Ramayana*, composed in Sanskrit by the sage Valmiki, is one of ancient India’s most revered epics. Spanning twenty-four thousand verses across seven books (*Kandas*), it narrates the life of Prince Rama, an avatar of Lord Vishnu, and serves as a timeless exploration of *dharma*—righteousness, duty, and devotion.

The story begins in the prosperous kingdom of Kosala, ruled from its capital, Ayodhya, by the noble King Dasharatha. Blessed with four sons across his three queens—Rama (born to Kaushalya), Bharata (born to Kaikeyi), and the twins Lakshmana and Shatrughna (born to Sumitra)—Dasharatha watches Rama grow into an embodiment of virtue and valour. In his youth, Rama accompanies the sage Vishwamitra to slay forest demons disrupting sacred rituals. Their journey leads to the kingdom of Mithila, where Rama strings and breaks the celestial bow of Lord Shiva, winning the hand of the wise and virtuous Princess Sita in marriage.

Years later, Dasharatha prepares to crown Rama as his successor. On the eve of the coronation, however, Queen Kaikeyi—instigated by her maid Manthara—redeems two past boons from the king. She demands that her son Bharata be crowned instead and that Rama be exiled to the forest for fourteen years. To honour his father’s word, Rama serenely accepts the decree, accompanied by his devoted wife Sita and loyal brother Lakshmana. Crushed by grief, Dasharatha soon passes away. Rejecting his mother’s scheme, Bharata refuses to claim the crown for himself; instead, he places Rama’s sandals upon the throne and rules Ayodhya strictly as a regent awaiting his brother’s return.

For years, the trio lives peacefully in the forest until Shurpanakha, sister of the ten-headed demon king Ravana of Lanka, tries to seduce the brothers at Panchavati and attacks Sita. After Lakshmana wounds Shurpanakha in defense, a furious Ravana plots vengeance. Using the shape-shifting demon Maricha disguised as a golden deer, Ravana lures Rama and Lakshmana away from their hermitage. Disguised as a mendicant, Ravana abducts Sita and carries her across the sea to Lanka, mortally wounding the noble vulture Jatayu, who bravely tries to save her.

Heartbroken, Rama and Lakshmana journey south to Kishkindha, forging an alliance with the exiled monkey prince Sugriva and his devoted minister, Lord Hanuman. After Rama helps Sugriva defeat his brother Vali to reclaim his throne, the Vanara army searches every direction for Sita. Hanuman leaps across the ocean to Lanka, finds Sita grieving in the Ashoka grove, comforts her with Rama’s signet ring, and sets parts of Lanka ablaze before returning to Rama with the news.

Joined by Sugriva’s army and Ravana’s righteous brother Vibhishana, Rama’s forces build a stone bridge—the Ram Setu—across the ocean and march on Lanka. In the fierce war that follows, Lakshmana slays Ravana’s son Indrajit, and Rama defeats the giant Kumbhakarna before finally vanquishing Ravana in battle, symbolizing the triumph of good over evil. With their exile concluded, Rama, Sita, and Lakshmana return to a lamp-lit Ayodhya—celebrated today as Diwali—ushering in *Rama Rajya*, a golden era of justice and peace."""

value = input("type any word you remember about ramayan:")
isfound = value in story
print(f"is{value} found", {isfound})

isfound = value not in story
print(f"is{value} not found", {isfound})

