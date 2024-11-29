const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/send-email', (req, res) => {
    let errorMSG = "";

    // NAME
    const name = req.body.name;
    if (!name) {
        errorMSG += "Name is required. ";
    }

    // EMAIL
    const email = req.body.email;
    if (!email) {
        errorMSG += "Email is required. ";
    }

    // Subject
    const subject = req.body.subject;
    if (!subject) {
        errorMSG += "Subject is required. ";
    }

    // MESSAGE
    const message = req.body.message;
    if (!message) {
        errorMSG += "Message is required. ";
    }

    const EmailTo = "armanmia7@gmail.com";
    const Subject = "New Message Received";

    // Prepare email body text
    const Body = 
        Name: ${name}
        Email: ${email}
        Subject: ${subject}
        Message: ${message}
    ;

    // Create reusable transporter object using the default SMTP transport
    const transporter = nodemailer.createTransport({
        service: 'gmail', // Используйте нужный вам сервис
        auth: {
            user: 'your-email@gmail.com', // Ваша почта
            pass: 'your-email-password' // Ваш пароль (или App Password)
        }
    });

    // Send email
    transporter.sendMail({
        from: email,
        to: EmailTo,
        subject: Subject,
        text: Body
    }, (error, info) => {
        if (error) {
            return res.status(500).send("Something went wrong :(");
        }
        if (errorMSG) {
            return res.status(400).send(errorMSG);
        }
        res.send("success");
    });
});

// Запуск сервера
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(Server is running on port ${PORT});
});
