
# Build the frontend 
FROM node:16-alpine as build-stage
WORKDIR /app
COPY package.json /app/package.json
COPY . /app
RUN npm install
RUN npm run build

# Set up Nginx server for serving static files 
FROM nginx:1.18
EXPOSE 80
COPY --from=build-stage /app/build/ /usr/share/nginx/html
