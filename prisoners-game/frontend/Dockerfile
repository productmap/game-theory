# Используем официальный образ Node.js
FROM node:22-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и устанавливаем зависимости
COPY package.json yarn.lock ./
RUN yarn install

# Копируем остальные файлы
COPY . .

# Сборка Next.js приложения
RUN yarn build

# Открываем порт 3000
EXPOSE 3000

# Запускаем Next.js приложение
CMD ["yarn", "start"]
