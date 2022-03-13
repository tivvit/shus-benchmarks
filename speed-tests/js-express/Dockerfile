FROM node:17

WORKDIR /app
ADD js-express/server.js server.js
ADD js-express/*.json ./

RUN npm install

CMD ["node", "server.js"]